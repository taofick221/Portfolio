(function(){
  const sidebar=document.getElementById("sidebar");
  document.getElementById("openMenu")?.addEventListener("click",()=>sidebar?.classList.add("open"));
  document.getElementById("closeMenu")?.addEventListener("click",()=>sidebar?.classList.remove("open"));
  document.querySelectorAll(".side-nav a").forEach(a=>a.addEventListener("click",()=>sidebar?.classList.remove("open")));

  const path=window.location.pathname;
  document.querySelectorAll(".side-nav a").forEach(a=>{
    const href=a.getAttribute("href")||"";
    if(path.startsWith("/projects") && href.startsWith("/projects/")) a.classList.add("active");
    if(path.startsWith("/contact") && href.startsWith("/contact")) a.classList.add("active");
  });
})();
