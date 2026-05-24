function navbar(){
    var elms = document.getElementsByClassName("header-main");
    if (window.matchMedia('screen and (max-width:675px)').matches) {
      // it matches
      console.log("j")
      Array.from(elms).forEach((x) => {
        if (x.style.display === "none") {
          x.style.display = "flex";
        } else {
          x.style.display = "none";
        }
      })
    } else {
      // does not match
      console.log("n")

    }
   



  }