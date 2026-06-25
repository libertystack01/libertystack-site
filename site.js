const nav = `
<header class="site-header">
  <nav class="nav" aria-label="Main navigation">
    <a class="brand" href="index.html" aria-label="LibertyStack home" data-brand>
      <img class="brand-logo" src="assets/logo.png" alt="LibertyStack logo">
      <span class="brand-text">LibertyStack <small>Solutions Private Limited</small></span>
    </a>
    <button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" data-nav-toggle>☰</button>
    <div class="nav-links" data-nav-links>
      <a href="about.html">About</a>
      <a href="services-pricing.html">Services &amp; Pricing</a>
      <a href="results.html">Our Results</a>
      <a href="testimonials.html">Testimonials</a>
      <a href="contact.html">Contact</a>
    </div>
  </nav>
</header>`;

const footer = `
<footer class="footer">
  <div class="footer-inner">
    <span>© 2026 LibertyStack Solutions Private Limited. Owned by Ishant.</span>
    <span><a href="tel:+917004625082">+91 7004625082</a> · <a href="contact.html">Contact</a></span>
  </div>
</footer>`;

document.body.insertAdjacentHTML("afterbegin", nav);
document.body.insertAdjacentHTML("beforeend", footer);

const page = document.body.dataset.page;
document.querySelectorAll(".nav-links a").forEach((a) => {
  if (a.getAttribute("href") === page) a.setAttribute("aria-current", "page");
});
