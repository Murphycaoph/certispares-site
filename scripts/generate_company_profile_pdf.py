from pathlib import Path
from textwrap import wrap

from reportlab.graphics import renderPDF
from reportlab.graphics.barcode import qr
from reportlab.graphics.shapes import Drawing
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from PIL import Image


ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "output" / "pdf"
TMP_DIR = ROOT / "tmp" / "pdfs"
IMAGES_DIR = ROOT / "public" / "images"
GENERATED_BRAND_LOGOS_DIR = IMAGES_DIR / "generated-brand-logos"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
TMP_DIR.mkdir(parents=True, exist_ok=True)
IMAGE_CACHE_DIR = TMP_DIR / "company-profile-assets"
IMAGE_CACHE_DIR.mkdir(parents=True, exist_ok=True)

PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 42

NAVY = colors.HexColor("#0A2540")
NAVY_DARK = colors.HexColor("#061735")
BLUE = colors.HexColor("#3957E9")
BLUE_2 = colors.HexColor("#2365FF")
GREEN = colors.HexColor("#0F9F67")
INK = colors.HexColor("#1D2A36")
TEXT = colors.HexColor("#30405D")
MUTED = colors.HexColor("#667085")
SOFT = colors.HexColor("#EEF5FC")
BG = colors.HexColor("#F7F9FC")
LINE = colors.HexColor("#DFE6E9")
WHITE = colors.white

EMAIL = "murphy@certispares.com"
WHATSAPP = "+86 156 3302 2618"
WEBSITE = "certispares.com"
SITE_URL = "https://certispares.com/"
COMPANY_CN = "北京盈好众源汽车配件有限公司"
FOOTER_TEXT = "CertiSpares | Commercial Vehicle Parts Sourcing from China"

HERO_IMAGE = IMAGES_DIR / "homepage" / "homepage-hero-truck.webp"
COVER_ALT_IMAGE = IMAGES_DIR / "hero-01-highway-transport.webp"
WHO_IMAGE = IMAGES_DIR / "china-industrial-warehouse.webp"
SUPPLIER_IMAGE = IMAGES_DIR / "factory-quality-inspection-metal-parts.webp"
SHIPMENT_IMAGE = IMAGES_DIR / "container-loading-supervision.webp"
CONTACT_IMAGE = IMAGES_DIR / "shipping-documents-export-paperwork.webp"
LOGO = IMAGES_DIR / "logo.webp"
COVER_LOGO_MARK = IMAGES_DIR / "certispares-logo-mark-white.png"

SUPPORTED_BRANDS = [
    ("Foton", "foton.webp"),
    ("HOWO", "howo.webp"),
    ("JAC", "jac.webp"),
    ("Dongfeng", "dongfeng.webp"),
    ("Sinotruk", "sinotruk.webp"),
    ("Shacman", "shacman.webp"),
    ("FAW", "faw.webp"),
    ("MAN", "man.webp"),
    ("Mercedes-Benz Truck", "mercedes-benz-truck.webp"),
    ("Volvo Truck", "volvo-truck.webp"),
]


try:
    simsun = Path("C:/Windows/Fonts/simsun.ttc")
    if simsun.exists():
        pdfmetrics.registerFont(TTFont("SimSunLocal", str(simsun), subfontIndex=0))
        CJK_FONT = "SimSunLocal"
    else:
        pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
        CJK_FONT = "STSong-Light"
except Exception:
    CJK_FONT = "Helvetica"


def image_path(primary: Path, fallback: Path | None = None) -> Path | None:
    if primary.exists():
        return primary
    if fallback and fallback.exists():
        return fallback
    return None


def optimized_image(path: Path) -> Path:
    if path == LOGO or path.suffix.lower() == ".png":
        return path
    cache_name = f"{path.stem[:70].replace(' ', '-')}-{path.stat().st_mtime_ns}.jpg"
    cached = IMAGE_CACHE_DIR / cache_name
    if cached.exists():
        return cached
    with Image.open(path) as img:
        img = img.convert("RGB")
        img.thumbnail((1500, 1500), Image.Resampling.LANCZOS)
        img.save(cached, "JPEG", quality=82, optimize=True, progressive=True)
    return cached


def white_logo_image() -> Path:
    cached = IMAGE_CACHE_DIR / "certispares-logo-white.png"
    if cached.exists():
        return cached
    with Image.open(LOGO) as img:
        img = img.convert("RGBA")
        pixels = img.load()
        for y in range(img.height):
            for x in range(img.width):
                r, g, b, a = pixels[x, y]
                if a > 12:
                    pixels[x, y] = (255, 255, 255, a)
        img.save(cached)
    return cached


def cover_logo_mark_image() -> Path:
    cached = IMAGE_CACHE_DIR / "certispares-cover-logo-mark-maskable.png"
    source = COVER_LOGO_MARK
    if cached.exists() and cached.stat().st_mtime_ns > source.stat().st_mtime_ns:
        return cached
    with Image.open(source) as img:
        img = img.convert("RGBA")
        out = Image.new("RGB", img.size, (0, 0, 0))
        src = img.load()
        dst = out.load()
        for y in range(img.height):
            for x in range(img.width):
                r, g, b, a = src[x, y]
                if a > 24 and (r + g + b) / 3 > 32:
                    dst[x, y] = (255, 255, 255)
        out.save(cached)
    return cached


def draw_cover_mark(c: canvas.Canvas, x: float, y: float, size: float):
    mark = cover_logo_mark_image()
    image = ImageReader(str(mark))
    c.drawImage(image, x, y, size, size, mask=[0, 8, 0, 8, 0, 8])


def fit_text(c: canvas.Canvas, text: str, font_name: str, max_size: int, min_size: int, width: float) -> int:
    size = max_size
    while size >= min_size:
        if c.stringWidth(text, font_name, size) <= width:
            return size
        size -= 1
    return min_size


def draw_wrapped_text(
    c: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    width: float,
    font_name: str = "Helvetica",
    font_size: int = 10,
    color: colors.Color = TEXT,
    leading: float | None = None,
    max_lines: int | None = None,
):
    leading = leading or font_size * 1.45
    lines: list[str] = []
    current = ""
    for word in text.split():
        candidate = word if not current else f"{current} {word}"
        if c.stringWidth(candidate, font_name, font_size) <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)

    if max_lines is not None and len(lines) > max_lines:
        lines = lines[:max_lines]
        last = lines[-1]
        while last and c.stringWidth(f"{last}...", font_name, font_size) > width:
            last = last[:-1]
        lines[-1] = f"{last.rstrip()}..."

    c.setFillColor(color)
    c.setFont(font_name, font_size)
    cursor = y
    for line in lines:
        c.drawString(x, cursor, line)
        cursor -= leading
    return cursor


def draw_clipped_image(
    c: canvas.Canvas,
    path: Path | None,
    x: float,
    y: float,
    width: float,
    height: float,
    mode: str = "cover",
    radius: float = 0,
):
    if not path or not path.exists():
        c.setFillColor(SOFT)
        c.roundRect(x, y, width, height, radius or 8, fill=1, stroke=0)
        c.setStrokeColor(LINE)
        c.roundRect(x, y, width, height, radius or 8, fill=0, stroke=1)
        return

    image = ImageReader(str(optimized_image(path)))
    iw, ih = image.getSize()
    if iw == 0 or ih == 0:
        return
    image_ratio = iw / ih
    box_ratio = width / height

    if mode == "cover":
        if image_ratio > box_ratio:
            draw_height = height
            draw_width = draw_height * image_ratio
        else:
            draw_width = width
            draw_height = draw_width / image_ratio
    else:
        if image_ratio > box_ratio:
            draw_width = width
            draw_height = draw_width / image_ratio
        else:
            draw_height = height
            draw_width = draw_height * image_ratio

    draw_x = x + (width - draw_width) / 2
    draw_y = y + (height - draw_height) / 2

    c.saveState()
    path_obj = c.beginPath()
    if radius:
        path_obj.roundRect(x, y, width, height, radius)
    else:
        path_obj.rect(x, y, width, height)
    c.clipPath(path_obj, stroke=0, fill=0)
    c.drawImage(image, draw_x, draw_y, draw_width, draw_height, mask="auto")
    c.restoreState()


def draw_logo(c: canvas.Canvas, x: float, y: float, width: float, height: float, on_dark: bool = False, plain_white: bool = False):
    if LOGO.exists():
        if plain_white:
            if COVER_LOGO_MARK.exists():
                draw_cover_mark(c, x, y, height)
            else:
                c.setFillColor(WHITE)
                c.setFont("Helvetica-Bold", 18)
                c.drawString(x, y + 20, "CertiSpares")
                c.setFont("Helvetica", 7.5)
                c.setFillColor(colors.Color(1, 1, 1, alpha=0.72))
                c.drawString(x + 1, y + 8, "COMMERCIAL VEHICLE PARTS SOURCING")
            return
        if on_dark:
            c.setFillColor(colors.Color(1, 1, 1, alpha=0.96))
            c.roundRect(x - 8, y - 5, width + 16, height + 10, 8, fill=1, stroke=0)
        draw_clipped_image(c, LOGO, x, y, width, height, mode="contain")
    else:
        c.setFillColor(WHITE if on_dark else NAVY)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(x, y + height / 2, "CertiSpares")


def draw_page_base(c: canvas.Canvas, page_no: int, title: str | None = None, dark: bool = False):
    if not dark:
        c.setFillColor(BG)
        c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.rect(0, PAGE_HEIGHT - 64, PAGE_WIDTH, 64, fill=1, stroke=0)
        c.setStrokeColor(LINE)
        c.line(MARGIN, PAGE_HEIGHT - 64, PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 64)
        draw_logo(c, MARGIN, PAGE_HEIGHT - 54, 132, 45)
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 8.5)
        c.drawRightString(PAGE_WIDTH - MARGIN, PAGE_HEIGHT - 35, FOOTER_TEXT)
    if title:
        c.setFillColor(INK if not dark else WHITE)
        c.setFont("Helvetica-Bold", 24)
        c.drawString(MARGIN, PAGE_HEIGHT - 106, title)
    draw_footer(c, page_no, dark=dark)


def draw_footer(c: canvas.Canvas, page_no: int, dark: bool = False):
    c.setStrokeColor(colors.Color(1, 1, 1, alpha=0.22) if dark else LINE)
    c.line(MARGIN, 30, PAGE_WIDTH - MARGIN, 30)
    c.setFillColor(colors.Color(1, 1, 1, alpha=0.78) if dark else MUTED)
    c.setFont("Helvetica", 8.5)
    c.drawString(MARGIN, 17, FOOTER_TEXT)
    c.drawRightString(PAGE_WIDTH - MARGIN, 17, f"{page_no:02d}")


def draw_section_label(c: canvas.Canvas, x: float, y: float, text: str, color: colors.Color = BLUE):
    c.setFillColor(color)
    c.roundRect(x, y - 6, c.stringWidth(text, "Helvetica-Bold", 8.5) + 18, 18, 7, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(x + 9, y, text)


def draw_card(c: canvas.Canvas, x: float, y: float, w: float, h: float, fill: colors.Color = WHITE):
    c.setFillColor(fill)
    c.roundRect(x, y, w, h, 8, fill=1, stroke=0)
    c.setStrokeColor(LINE)
    c.roundRect(x, y, w, h, 8, fill=0, stroke=1)


def draw_bullet(c: canvas.Canvas, x: float, y: float, text: str, width: float, color: colors.Color = TEXT):
    c.setFillColor(BLUE)
    c.circle(x + 3, y + 4, 2.4, fill=1, stroke=0)
    return draw_wrapped_text(c, text, x + 13, y, width - 13, "Helvetica", 9.5, color, leading=13)


def draw_icon_circle(c: canvas.Canvas, x: float, y: float, label: str, fill: colors.Color = BLUE):
    c.setFillColor(fill)
    c.circle(x, y, 16, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(x, y - 3, label)


def draw_qr(c: canvas.Canvas, data: str, x: float, y: float, size: float):
    qr_code = qr.QrCodeWidget(data)
    bounds = qr_code.getBounds()
    qr_w = bounds[2] - bounds[0]
    qr_h = bounds[3] - bounds[1]
    drawing = Drawing(size, size)
    group = qr_code.draw()
    group.scale(size / qr_w, size / qr_h)
    drawing.add(group)
    renderPDF.draw(drawing, c, x, y)


def draw_image_edge_fade(c: canvas.Canvas, x: float, y: float, width: float, height: float, bg_color: colors.Color = BG):
    steps = 16
    max_alpha = 0.98
    for i in range(steps):
        alpha = max_alpha * ((i + 1) / steps) ** 1.4
        inset = i * 3.5
        edge_h = max(3, 26 - i * 1.1)
        c.setFillColor(colors.Color(bg_color.red, bg_color.green, bg_color.blue, alpha=alpha))
        c.rect(x + inset, y + height - edge_h, width - inset * 2, edge_h, fill=1, stroke=0)
        c.rect(x + inset, y, width - inset * 2, edge_h, fill=1, stroke=0)
        c.rect(x, y + inset, edge_h, height - inset * 2, fill=1, stroke=0)
        c.rect(x + width - edge_h, y + inset, edge_h, height - inset * 2, fill=1, stroke=0)


def draw_cover(c: canvas.Canvas):
    hero = image_path(HERO_IMAGE, COVER_ALT_IMAGE)
    draw_clipped_image(c, hero, 0, 0, PAGE_WIDTH, PAGE_HEIGHT, mode="cover")
    c.setFillColor(colors.Color(6 / 255, 23 / 255, 53 / 255, alpha=0.86))
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    c.setFillColor(colors.Color(57 / 255, 87 / 255, 233 / 255, alpha=0.22))
    c.rect(0, 0, PAGE_WIDTH, PAGE_HEIGHT, fill=1, stroke=0)
    c.setFillAlpha(1)
    c.setStrokeAlpha(1)

    draw_logo(c, MARGIN, PAGE_HEIGHT - 112, 52, 52, plain_white=True)
    draw_section_label(c, MARGIN, PAGE_HEIGHT - 156, "B2B SOURCING INTRODUCTION", BLUE)

    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 43)
    c.drawString(MARGIN, PAGE_HEIGHT - 226, "CertiSpares")

    subtitle = "Commercial Vehicle Parts Sourcing from China"
    size = fit_text(c, subtitle, "Helvetica-Bold", 27, 20, PAGE_WIDTH - 2 * MARGIN)
    c.setFont("Helvetica-Bold", size)
    c.drawString(MARGIN, PAGE_HEIGHT - 268, subtitle)

    draw_wrapped_text(
        c,
        "A practical sourcing partner for overseas buyers who need clearer communication, supplier comparison, and order execution support.",
        MARGIN,
        PAGE_HEIGHT - 306,
        385,
        "Helvetica",
        13,
        colors.Color(1, 1, 1, alpha=0.88),
        leading=18,
    )

    c.setFillColor(colors.Color(1, 1, 1, alpha=0.12))
    c.roundRect(MARGIN, 158, 326, 118, 8, fill=1, stroke=0)
    bullets = [
        "RFQ clarification before quotation",
        "Supplier comparison and order follow-up",
        "Mixed-SKU sourcing and shipment coordination",
    ]
    y = 236
    for item in bullets:
        c.setFillColor(colors.Color(1, 1, 1, alpha=0.92))
        c.setFont("Helvetica", 11)
        c.drawString(MARGIN + 24, y, item)
        c.setFillColor(GREEN)
        c.circle(MARGIN + 10, y + 4, 3, fill=1, stroke=0)
        y -= 28

    c.setFillColor(WHITE)
    c.roundRect(PAGE_WIDTH - MARGIN - 184, 92, 184, 96, 8, fill=1, stroke=0)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(PAGE_WIDTH - MARGIN - 164, 158, "Send Your RFQ")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 9.5)
    c.drawString(PAGE_WIDTH - MARGIN - 164, 132, WHATSAPP)
    c.drawString(PAGE_WIDTH - MARGIN - 164, 110, EMAIL)

    draw_footer(c, 1, dark=True)
    c.showPage()


def draw_who_we_are(c: canvas.Canvas):
    draw_page_base(c, 2, "Who We Are")
    left_w = 285
    draw_section_label(c, MARGIN, PAGE_HEIGHT - 138, "RFQ-FIRST SOURCING SUPPORT", BLUE)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(MARGIN, PAGE_HEIGHT - 178, "A practical China sourcing desk")
    c.drawString(MARGIN, PAGE_HEIGHT - 202, "for commercial vehicle aftermarket")
    c.drawString(MARGIN, PAGE_HEIGHT - 226, "buyers.")
    draw_wrapped_text(
        c,
        "CertiSpares helps importers, distributors, wholesalers, and fleet-related buyers turn scattered part numbers, photos, supplier replies, and mixed lists into clearer sourcing decisions.",
        MARGIN,
        PAGE_HEIGHT - 256,
        left_w,
        "Helvetica",
        11,
        TEXT,
        leading=16,
    )
    draw_wrapped_text(
        c,
        "CertiSpares works as a sourcing and execution support desk, helping buyers clarify inquiries, compare supplier options, and follow up order details.",
        MARGIN,
        PAGE_HEIGHT - 342,
        left_w,
        "Helvetica-Bold",
        11,
        NAVY,
        leading=16,
    )

    draw_clipped_image(c, image_path(WHO_IMAGE, IMAGES_DIR / "auto-parts-warehouse-shelves.webp"), PAGE_WIDTH - MARGIN - 164, PAGE_HEIGHT - 320, 164, 188, "cover", 8)

    items = [
        ("01", "Commercial vehicle aftermarket and replacement parts"),
        ("02", "RFQ clarification before quotation"),
        ("03", "Supplier comparison and order follow-up"),
        ("04", "Mixed-SKU and multi-supplier sourcing"),
        ("05", "Packing, documents, inspection points, and shipment coordination"),
    ]
    y = 430
    for code, text in items:
        draw_card(c, MARGIN, y - 38, PAGE_WIDTH - 2 * MARGIN, 46, WHITE)
        draw_icon_circle(c, MARGIN + 28, y - 15, code, BLUE)
        draw_wrapped_text(c, text, MARGIN + 58, y - 10, PAGE_WIDTH - 2 * MARGIN - 78, "Helvetica-Bold", 10.5, INK, leading=13)
        y -= 56

    c.showPage()


def draw_source_scope(c: canvas.Canvas):
    draw_page_base(c, 3, "What We Help Buyers Source")
    categories = [
        ("Engine Parts", "Filters, belts, pumps, sensors, gaskets, mounts, and selected repair items."),
        ("Brake System Parts", "Brake chambers, drums, linings, valves, slack adjusters, and repair kits."),
        ("Suspension Parts", "Leaf springs, torque rods, stabilizer parts, bushings, shocks, and hardware."),
        ("Axle & Wheel-end Parts", "Hubs, bearings, seals, wheel bolts, king pins, and wheel-end repair items."),
        ("Gearbox & Transmission", "Clutch parts, gearbox repair items, bearings, seals, and shift-related parts."),
        ("Air System Parts", "Air valves, dryers, compressors, tanks, hoses, connectors, and pneumatic parts."),
        ("Cooling System Parts", "Radiators, intercoolers, fan clutches, water pumps, hoses, and thermostats."),
        ("Rubber & Bushing Parts", "Mounts, bushings, rubber pads, seals, flexible joints, and related parts."),
    ]
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 11)
    c.drawString(MARGIN, PAGE_HEIGHT - 132, "Major systems and product families used as RFQ entry points, not as a full SKU catalogue.")

    cols = 2
    gap = 16
    card_w = (PAGE_WIDTH - 2 * MARGIN - gap) / cols
    card_h = 88
    y0 = PAGE_HEIGHT - 246
    for i, (title, text) in enumerate(categories):
        col = i % cols
        row = i // cols
        x = MARGIN + col * (card_w + gap)
        y = y0 - row * (card_h + 16)
        draw_card(c, x, y, card_w, card_h, WHITE)
        draw_icon_circle(c, x + 24, y + card_h - 22, f"{i + 1}", GREEN if i % 3 == 0 else BLUE)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(x + 50, y + card_h - 26, title)
        draw_wrapped_text(c, text, x + 18, y + card_h - 52, card_w - 36, "Helvetica", 9.5, MUTED, leading=13, max_lines=3)

    image = image_path(IMAGES_DIR / "auto-parts-warehouse-shelves.webp", IMAGES_DIR / "homepage" / "homepage-part-confirmation.webp")
    band_x = MARGIN
    band_y = 92
    band_w = PAGE_WIDTH - 2 * MARGIN
    band_h = 128
    image_w = 250
    draw_card(c, band_x, band_y, band_w, band_h, WHITE)
    c.saveState()
    clip = c.beginPath()
    clip.roundRect(band_x, band_y, band_w, band_h, 8)
    c.clipPath(clip, stroke=0, fill=0)
    c.setFillColor(NAVY)
    c.rect(band_x, band_y, band_w - image_w + 26, band_h, fill=1, stroke=0)
    draw_clipped_image(c, image, band_x + band_w - image_w, band_y, image_w, band_h, "cover", 0)
    c.setFillColor(colors.Color(10 / 255, 37 / 255, 64 / 255, alpha=0.18))
    c.rect(band_x + band_w - image_w, band_y, image_w, band_h, fill=1, stroke=0)
    c.restoreState()
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(band_x + 22, band_y + 82, "RFQ scope starts from systems.")
    draw_wrapped_text(
        c,
        "Buyers can begin with a part family, a mixed list, a vehicle platform, or photos. We organize the inquiry before supplier comparison.",
        band_x + 22,
        band_y + 56,
        band_w - image_w - 22,
        "Helvetica",
        9.6,
        colors.Color(1, 1, 1, alpha=0.86),
        leading=13,
        max_lines=3,
    )

    c.showPage()


def draw_supported_brands(c: canvas.Canvas):
    draw_page_base(c, 4, "Supported Brand Inquiry Scope")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 11)
    c.drawString(MARGIN, PAGE_HEIGHT - 132, "Common brand references used as RFQ starting points. Coverage is not limited to these brands.")

    cols = 5
    rows = 2
    gap_x = 12
    gap_y = 18
    card_w = (PAGE_WIDTH - 2 * MARGIN - gap_x * (cols - 1)) / cols
    card_h = card_w
    start_y = PAGE_HEIGHT - 260

    for index, (brand, file_name) in enumerate(SUPPORTED_BRANDS):
        col = index % cols
        row = index // cols
        x = MARGIN + col * (card_w + gap_x)
        y = start_y - row * (card_h + gap_y)
        draw_card(c, x, y, card_w, card_h, WHITE)
        logo_path = GENERATED_BRAND_LOGOS_DIR / file_name
        draw_clipped_image(c, logo_path, x + 10, y + 26, card_w - 20, card_h - 52, "contain", 0)

    draw_wrapped_text(
        c,
        "If you need parts for a brand or platform not shown here, send your RFQ with the model, VIN, OE number, photos, or old supplier reference. We can review whether the inquiry is workable.",
        MARGIN,
        304,
        PAGE_WIDTH - 2 * MARGIN,
        "Helvetica-Bold",
        10,
        NAVY,
        leading=14,
        max_lines=2,
    )

    band_y = 138
    band_h = 124
    draw_card(c, MARGIN, band_y, PAGE_WIDTH - 2 * MARGIN, band_h, SOFT)
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 15)
    c.drawString(MARGIN + 22, band_y + 78, "Brand names help start the inquiry.")
    draw_wrapped_text(
        c,
        "They are not automatic fitment conclusions. Buyers can send brand, model, VIN, OE number, photos, or old supplier references so we can clarify the matching scope before supplier comparison.",
        MARGIN + 22,
        band_y + 52,
        PAGE_WIDTH - 2 * MARGIN - 44,
        "Helvetica",
        10,
        TEXT,
        leading=14,
        max_lines=3,
    )
    c.showPage()


def draw_inquiry_types(c: canvas.Canvas):
    draw_page_base(c, 5, "Supported Inquiry Types")
    draw_card(c, MARGIN, PAGE_HEIGHT - 214, PAGE_WIDTH - 2 * MARGIN, 84, SOFT)
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(MARGIN + 22, PAGE_HEIGHT - 162, "You do not need a perfect RFQ to start.")
    draw_wrapped_text(
        c,
        "If some details are missing, we separate confirmed items from items that need checking before supplier comparison.",
        MARGIN + 22,
        PAGE_HEIGHT - 183,
        PAGE_WIDTH - 2 * MARGIN - 44,
        "Helvetica",
        10.5,
        TEXT,
        leading=14,
    )

    items = [
        "OE number or supplier part number",
        "VIN, chassis number, vehicle model, or platform",
        "Product photos, labels, packaging, or old samples",
        "Old supplier reference or quotation sheet",
        "Mixed parts list, Excel file, PDF, or screenshots",
        "Sample request or replacement discussion",
        "Quantity, destination country, destination port, or packing notes",
    ]
    left_x = MARGIN
    right_x = PAGE_WIDTH - MARGIN - 220
    draw_clipped_image(c, image_path(CONTACT_IMAGE, IMAGES_DIR / "shipping-documents-export-paperwork.webp"), right_x, 118, 220, 326, "cover", 8)

    y = PAGE_HEIGHT - 262
    for i, item in enumerate(items):
        draw_card(c, left_x, y - 37, 286, 46, WHITE)
        draw_icon_circle(c, left_x + 25, y - 14, f"{i + 1}", BLUE)
        draw_wrapped_text(c, item, left_x + 56, y - 9, 210, "Helvetica-Bold", 10, INK, leading=12.5, max_lines=2)
        y -= 54

    c.showPage()


def draw_how_we_work(c: canvas.Canvas):
    draw_page_base(c, 6, "How We Work")
    steps = [
        ("Buyer sends inquiry", "Send part numbers, photos, lists, quantities, vehicle details, and destination."),
        ("We clarify part details", "We check matching risks, visible specifications, photos, and missing information."),
        ("We check supplier options", "We look for workable suppliers based on category fit and execution ability."),
        ("We compare quote basis", "Price, MOQ, lead time, quality level, packing, and response quality are compared together."),
        ("We support execution", "Order follow-up, inspection points, packing, documents, and shipment coordination stay visible."),
    ]
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 11)
    c.drawString(MARGIN, PAGE_HEIGHT - 132, "A simple flow for moving from incomplete inquiry to workable sourcing execution.")

    x_line = MARGIN + 36
    start_y = PAGE_HEIGHT - 218
    step_gap = 88
    last_y = start_y - step_gap * (len(steps) - 1)
    c.setStrokeColor(BLUE)
    c.setLineWidth(2)
    c.line(x_line, start_y + 16, x_line, last_y - 16)
    y = start_y
    for i, (title, desc) in enumerate(steps):
        draw_icon_circle(c, x_line, y, f"{i + 1}", BLUE if i < 4 else GREEN)
        draw_card(c, MARGIN + 74, y - 34, PAGE_WIDTH - MARGIN * 2 - 74, 72, WHITE)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 13)
        c.drawString(MARGIN + 96, y + 12, title)
        draw_wrapped_text(c, desc, MARGIN + 96, y - 10, PAGE_WIDTH - MARGIN * 2 - 118, "Helvetica", 10, MUTED, leading=14, max_lines=2)
        y -= 88

    c.showPage()


def draw_why_buyers(c: canvas.Canvas):
    draw_page_base(c, 7, "Why Buyers Use CertiSpares")
    left = MARGIN
    right = PAGE_WIDTH / 2 + 10
    col_w = PAGE_WIDTH / 2 - MARGIN - 20
    draw_section_label(c, left, PAGE_HEIGHT - 162, "COMMON SOURCING PROBLEMS", NAVY)
    draw_section_label(c, right, PAGE_HEIGHT - 162, "WHAT WE HELP ORGANIZE", GREEN)
    problems = [
        "One buyer may need parts from different suppliers.",
        "OE numbers and vehicle models are often unclear.",
        "Supplier replies may not follow the same quote basis.",
        "Small and mixed orders need more coordination.",
        "Buyers need photos, confirmation records, and shipment updates.",
    ]
    values = [
        "Clearer inquiry handling",
        "Supplier comparison on the same basis",
        "Consolidated communication",
        "Practical execution tracking",
        "More traceable confirmation before shipment",
    ]
    y = PAGE_HEIGHT - 214
    for item in problems:
        y = draw_bullet(c, left, y, item, col_w) - 14

    y = PAGE_HEIGHT - 214
    for item in values:
        draw_card(c, right, y - 34, col_w, 42, WHITE)
        c.setFillColor(GREEN)
        c.circle(right + 17, y - 13, 5, fill=1, stroke=0)
        draw_wrapped_text(c, item, right + 32, y - 9, col_w - 48, "Helvetica-Bold", 10.5, INK, leading=13)
        y -= 55

    draw_clipped_image(c, image_path(IMAGES_DIR / "sourcing" / "compare-warehouse-team.webp", SUPPLIER_IMAGE), MARGIN, 92, PAGE_WIDTH - 2 * MARGIN, 168, "cover", 8)
    c.setFillColor(colors.Color(6 / 255, 23 / 255, 53 / 255, alpha=0.72))
    c.roundRect(MARGIN, 92, PAGE_WIDTH - 2 * MARGIN, 168, 8, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(MARGIN + 24, 202, "The goal is not only to quote.")
    draw_wrapped_text(
        c,
        "The goal is to make the sourcing path clear enough for a buyer to decide, confirm, order, and repeat with fewer avoidable mistakes.",
        MARGIN + 24,
        174,
        PAGE_WIDTH - 2 * MARGIN - 48,
        "Helvetica",
        11,
        colors.Color(1, 1, 1, alpha=0.9),
        leading=16,
    )
    c.showPage()


def draw_supplier_comparison(c: canvas.Canvas):
    draw_page_base(c, 8, "Supplier Comparison & Confirmation")
    draw_clipped_image(c, image_path(SUPPLIER_IMAGE, IMAGES_DIR / "engineering-quality-control-lab.webp"), MARGIN, PAGE_HEIGHT - 342, PAGE_WIDTH - 2 * MARGIN, 176, "cover", 8)
    c.setFillColor(colors.Color(10 / 255, 37 / 255, 64 / 255, alpha=0.68))
    c.roundRect(MARGIN, PAGE_HEIGHT - 342, PAGE_WIDTH - 2 * MARGIN, 176, 8, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 19)
    c.drawString(MARGIN + 24, PAGE_HEIGHT - 234, "We do not treat the first fast quote")
    c.drawString(MARGIN + 24, PAGE_HEIGHT - 258, "as the final answer.")
    draw_wrapped_text(
        c,
        "Key details should be checked before payment and shipment, especially when OE number, model, photos, or dimensions need further confirmation.",
        MARGIN + 24,
        PAGE_HEIGHT - 286,
        390,
        "Helvetica",
        10.5,
        colors.Color(1, 1, 1, alpha=0.9),
        leading=15,
    )

    items = [
        "Price level",
        "MOQ and lead time",
        "Product photos and visible details",
        "Brand or aftermarket quality level",
        "Packing method and carton marks",
        "Supplier response quality",
        "Order size and shipment practicality",
    ]
    cols = 2
    gap = 14
    card_w = (PAGE_WIDTH - 2 * MARGIN - gap) / cols
    y0 = PAGE_HEIGHT - 400
    for i, item in enumerate(items):
        col = i % cols
        row = i // cols
        x = MARGIN + col * (card_w + gap)
        y = y0 - row * 56
        draw_card(c, x, y - 34, card_w, 42, WHITE)
        draw_icon_circle(c, x + 22, y - 13, f"{i + 1}", BLUE)
        draw_wrapped_text(c, item, x + 50, y - 9, card_w - 62, "Helvetica-Bold", 10, INK, leading=13, max_lines=2)

    c.showPage()


def draw_order_shipment(c: canvas.Canvas):
    draw_page_base(c, 9, "Order & Shipment Support")
    left_w = 250
    draw_clipped_image(c, image_path(SHIPMENT_IMAGE, IMAGES_DIR / "container-stacking-yard-sunset.webp"), MARGIN, PAGE_HEIGHT - 372, left_w, 238, "cover", 8)
    draw_card(c, MARGIN + left_w + 22, PAGE_HEIGHT - 372, PAGE_WIDTH - 2 * MARGIN - left_w - 22, 238, WHITE)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(MARGIN + left_w + 44, PAGE_HEIGHT - 176, "After supplier selection,")
    c.drawString(MARGIN + left_w + 44, PAGE_HEIGHT - 200, "execution still matters.")
    draw_wrapped_text(
        c,
        "CertiSpares can support order follow-up, packing visibility, document coordination, freight communication, and shipment status based on the agreed trade terms and buyer needs.",
        MARGIN + left_w + 44,
        PAGE_HEIGHT - 234,
        PAGE_WIDTH - 2 * MARGIN - left_w - 68,
        "Helvetica",
        10.5,
        TEXT,
        leading=15,
    )

    items = [
        ("01", "Mixed-order consolidation"),
        ("02", "Pre-shipment photos"),
        ("03", "Packing and label confirmation"),
        ("04", "Export document coordination"),
        ("05", "Freight option communication"),
        ("06", "Shipment status follow-up"),
    ]
    cols = 2
    gap = 16
    card_w = (PAGE_WIDTH - 2 * MARGIN - gap) / cols
    y0 = PAGE_HEIGHT - 444
    for i, (code, title) in enumerate(items):
        col = i % cols
        row = i // cols
        x = MARGIN + col * (card_w + gap)
        y = y0 - row * 64
        draw_card(c, x, y - 38, card_w, 48, WHITE)
        draw_icon_circle(c, x + 24, y - 14, code, GREEN if i >= 3 else BLUE)
        draw_wrapped_text(c, title, x + 54, y - 10, card_w - 70, "Helvetica-Bold", 10.5, INK, leading=13, max_lines=2)

    c.showPage()


def draw_typical_buyers(c: canvas.Canvas):
    draw_page_base(c, 10, "Typical Buyers We Serve")
    buyers = [
        ("Truck parts importers", "Need workable supplier options and clearer repeat-order communication."),
        ("Aftermarket distributors", "Manage mixed SKUs across brake, suspension, engine, cooling, rubber, and electrical items."),
        ("Repair workshop suppliers", "Need practical sourcing for common replacement and service parts."),
        ("Fleet maintenance buyers", "Care about correct matching, order visibility, and fewer avoidable delays."),
        ("Regional trading companies", "Need China sourcing support, supplier comparison, and shipment follow-up."),
        ("Buyers sourcing Chinese commercial vehicle parts", "Need help turning incomplete information into a workable RFQ."),
    ]
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 11)
    c.drawString(MARGIN, PAGE_HEIGHT - 132, "Built for buyers who need practical sourcing support, not a generic catalogue attachment.")

    y = PAGE_HEIGHT - 224
    for i, (title, desc) in enumerate(buyers):
        draw_card(c, MARGIN, y - 50, PAGE_WIDTH - 2 * MARGIN, 60, WHITE)
        draw_icon_circle(c, MARGIN + 28, y - 20, f"{i + 1}", BLUE if i % 2 == 0 else GREEN)
        c.setFillColor(INK)
        c.setFont("Helvetica-Bold", 12)
        c.drawString(MARGIN + 62, y - 9, title)
        draw_wrapped_text(c, desc, MARGIN + 62, y - 28, PAGE_WIDTH - 2 * MARGIN - 84, "Helvetica", 9.5, MUTED, leading=13, max_lines=2)
        y -= 72

    c.showPage()


def draw_contact(c: canvas.Canvas):
    draw_page_base(c, 11, "Send Your Parts Inquiry")
    top_y = PAGE_HEIGHT - 332
    top_h = 206
    draw_card(c, MARGIN, top_y, PAGE_WIDTH - 2 * MARGIN, top_h, WHITE)
    c.setFillColor(INK)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(MARGIN + 22, top_y + top_h - 38, "To help us reply faster, send:")
    items = [
        "Part number or OE number",
        "Vehicle model or VIN if available",
        "Product photos",
        "Quantity",
        "Destination country or port",
        "Preferred quality level or budget range",
        "Packing, label, or shipping notes",
    ]
    col_w = (PAGE_WIDTH - 2 * MARGIN - 58) / 2
    for index, item in enumerate(items):
        col = index % 2
        row = index // 2
        x = MARGIN + 22 + col * (col_w + 28)
        y = top_y + top_h - 78 - row * 30
        draw_bullet(c, x, y, item, col_w)

    contact_y = 194
    contact_h = 222
    draw_card(c, MARGIN, contact_y, PAGE_WIDTH - 2 * MARGIN, contact_h, WHITE)
    image_x = MARGIN
    image_w = PAGE_WIDTH - 2 * MARGIN
    draw_clipped_image(c, image_path(CONTACT_IMAGE, IMAGES_DIR / "shipping-documents-export-paperwork.webp"), image_x, contact_y, image_w, contact_h, "cover", 8)
    c.setFillColor(colors.Color(6 / 255, 23 / 255, 53 / 255, alpha=0.82))
    c.roundRect(MARGIN, contact_y, PAGE_WIDTH - 2 * MARGIN, contact_h, 8, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 19)
    c.drawString(MARGIN + 24, contact_y + contact_h - 44, "Contact Us")
    c.setFont("Helvetica", 11)
    c.drawString(MARGIN + 24, contact_y + contact_h - 84, f"WhatsApp: {WHATSAPP}")
    c.drawString(MARGIN + 24, contact_y + contact_h - 112, f"Email: {EMAIL}")
    c.drawString(MARGIN + 24, contact_y + contact_h - 140, f"Website: {WEBSITE}")
    c.drawString(MARGIN + 24, contact_y + contact_h - 168, "Company name:")
    c.setFont(CJK_FONT, 11)
    c.drawString(MARGIN + 112, contact_y + contact_h - 168, COMPANY_CN)
    c.setFillColor(WHITE)
    qr_size = 92
    qr_x = PAGE_WIDTH - MARGIN - qr_size - 38
    qr_y = contact_y + contact_h - 144
    c.roundRect(qr_x - 12, qr_y - 12, qr_size + 24, qr_size + 24, 8, fill=1, stroke=0)
    draw_qr(c, SITE_URL, qr_x, qr_y, qr_size)

    note_y = 68
    note_h = 76
    draw_card(c, MARGIN, note_y, PAGE_WIDTH - 2 * MARGIN, note_h, SOFT)
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(MARGIN + 14, note_y + note_h - 22, "Fitment and inquiry note")
    disclaimer = (
        "Brand names, OE numbers, vehicle models, and cross references are used for inquiry identification only. "
        "Final fitment and quotation scope must be confirmed by OE reference, VIN, model/year/market data, dimensions, connector type, "
        "and other applicable technical specifications."
    )
    draw_wrapped_text(c, disclaimer, MARGIN + 14, note_y + note_h - 40, PAGE_WIDTH - 2 * MARGIN - 28, "Helvetica", 6.8, TEXT, leading=9)

    c.showPage()


def main():
    output = OUTPUT_DIR / "CertiSpares-Company-Profile.pdf"
    c = canvas.Canvas(str(output), pagesize=A4)
    c.setTitle("CertiSpares Company Profile")
    c.setAuthor("CertiSpares")
    c.setSubject("Commercial Vehicle Parts Sourcing from China")

    draw_cover(c)
    draw_who_we_are(c)
    draw_source_scope(c)
    draw_supported_brands(c)
    draw_inquiry_types(c)
    draw_how_we_work(c)
    draw_why_buyers(c)
    draw_supplier_comparison(c)
    draw_order_shipment(c)
    draw_typical_buyers(c)
    draw_contact(c)
    c.save()
    print(output)


if __name__ == "__main__":
    main()
