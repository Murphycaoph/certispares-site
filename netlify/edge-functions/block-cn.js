const blockedCountries = new Set(["CN"]);

export default async (_request, context) => {
  const countryCode = context.geo?.country?.code?.toUpperCase();

  if (blockedCountries.has(countryCode)) {
    return new Response("Access denied.", {
      status: 403,
      headers: {
        "content-type": "text/plain; charset=utf-8",
        "cache-control": "no-store",
      },
    });
  }
};
