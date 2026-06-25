# LibertyStack Ready Site

This folder is ready to replace the files in the GitHub Pages repository.

## Website files

Upload everything in this folder except `backend/` to the GitHub Pages repo root:

- `index.html`
- `about.html`
- `services-pricing.html`
- `results.html`
- `testimonials.html`
- `contact.html`
- `styles.css`
- `site.js`
- `script.js`
- `assets/`
- `CNAME`
- `robots.txt`
- `sitemap.xml`

The menu links now point to real subpages.

## Contact backend

The `backend/` folder is for a separate Vercel project. Deploy only that folder to Vercel.

Set these Vercel environment variables:

- `ZOHO_SMTP_HOST=smtp.zoho.in`
- `ZOHO_SMTP_PORT=465`
- `ZOHO_SMTP_USER=` your support mailbox address
- `ZOHO_SMTP_PASS=` your Zoho app password, not your main password
- `CONTACT_TO=ishant@libertystack.co.in`

After Vercel gives you a URL, edit `index.html` and `contact.html` and replace:

`https://YOUR-VERCEL-PROJECT.vercel.app/api/contact`

with your real Vercel endpoint, for example:

`https://libertystack-contact.vercel.app/api/contact`

The support sender is not visible on the website. It only lives in Vercel environment variables.
