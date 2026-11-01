// Menu mobile: un solo script per tutte le pagine
document.addEventListener("DOMContentLoaded", function () {
  const menuToggle = document.getElementById("menu-toggle");
  const navLinks   = document.getElementById("nav-links");
  if (!menuToggle || !navLinks) return;

  const isOpen = () => navLinks.classList.contains("active");
  const openMenu = () => {
    navLinks.classList.add("active");
    document.body.classList.add("menu-open");
    menuToggle.setAttribute("aria-expanded", "true");
  };
  const closeMenu = () => {
    navLinks.classList.remove("active");
    document.body.classList.remove("menu-open");
    menuToggle.setAttribute("aria-expanded", "false");
  };

  // clic (o Invio/Spazio da tastiera, perché è un <button>)
  menuToggle.addEventListener("click", (e) => {
    e.stopPropagation();
    isOpen() ? closeMenu() : openMenu();
  });

  // chiudi quando si sceglie una voce
  navLinks.querySelectorAll("a").forEach(a => a.addEventListener("click", closeMenu));

  // chiudi cliccando fuori dal menu
  document.addEventListener("click", (e) => {
    if (isOpen() && !navLinks.contains(e.target) && !menuToggle.contains(e.target)) closeMenu();
  });

  // chiudi con ESC e riporta il focus sul pulsante
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && isOpen()) { closeMenu(); menuToggle.focus(); }
  });

  // chiudi allo scroll della pagina, al cambio di ancora e tornando a desktop
  window.addEventListener("scroll", () => { if (isOpen()) closeMenu(); }, { passive: true });
  window.addEventListener("hashchange", closeMenu);
  window.addEventListener("resize", () => { if (window.innerWidth > 992 && isOpen()) closeMenu(); });
});
