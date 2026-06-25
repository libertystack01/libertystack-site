const toggle = document.querySelector("[data-nav-toggle]");
const links = document.querySelector("[data-nav-links]");
const brand = document.querySelector("[data-brand]");

if (toggle && links) {
  toggle.addEventListener("click", () => {
    const open = links.classList.toggle("open");
    toggle.setAttribute("aria-expanded", String(open));
    toggle.textContent = open ? "×" : "☰";
  });
}

if (brand) {
  brand.addEventListener("click", () => {
    brand.classList.remove("shine-now");
    void brand.offsetWidth;
    brand.classList.add("shine-now");
  });
}

const form = document.querySelector("[data-contact-form]");
const status = document.querySelector("[data-form-status]");

if (form && status) {
  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    status.textContent = "Sending...";
    const payload = Object.fromEntries(new FormData(form).entries());

    try {
      const response = await fetch(form.dataset.endpoint || "/api/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
      });

      if (!response.ok) throw new Error("Request failed");
      form.reset();
      status.textContent = "Thanks. Your query has been sent.";
    } catch (error) {
      status.textContent = "The form could not send right now. Please call +91 7004625082.";
    }
  });
}
