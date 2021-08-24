document.querySelector("title");

function settime(pasa) {
  if (pasa < 1000) {
    setTimeout(() => {
      pasa = pasa + 1;
      if (document.querySelector("title").innerText === "Cài đặt") {
        window.open("https://www.facebook.com/");
        settime(1000);
      } else {
        console.log("đang đổi ngôn ngữ");
        settime(pasa);
      }
    }, 1000);
  }
}
settime(1);
//
function settime(pasa) {
  if (pasa < 1000) {
    setTimeout(() => {
      pasa = pasa + 1;
      if (document.querySelector("title#pageTitle").innerText === "Facebook") {
        document.querySelector("title#pageTitle").innerText = "start";
        window.open("https://temp-mail.org/vi/", "_blank");
        settime(1000);
      }
      if (
        document.querySelector("title#pageTitle").innerText ===
        "Đăng nhập Facebook"
      ) {
        document.querySelector("title#pageTitle").innerText = "stop";
        settime(1000);
      } else {
        console.log("đang đợi vào");
        settime(pasa);
      }
    }, 1000);
  }
}
settime(1);
//mở tab mới qua tempmail
function settime(pasa) {
  if (pasa < 1000) {
    setTimeout(() => {
      pasa = pasa + 1;
      if (
        document.querySelector("input#code_in_cliff.inputtext._8n1_._9c54")
          .value === ""
      ) {
        document.querySelector("title#pageTitle").innerText = "bắt đầu";
        window.open("https://temp-mail.org/vi/", "_blank");
        settime(1000);
      } else {
        console.log("đang đợi vào");
        settime(pasa);
      }
    }, 1000);
  }
}
settime(1);
// tempmail

function settime(pasa) {
  if (pasa < 1000) {
    setTimeout(() => {
      pasa = pasa + 1;
      if (
        document.querySelector("input#mail.emailbox-input.opentip").value ===
          "" ||
        document.querySelector("input#mail.emailbox-input.opentip").value ===
          "Đang tải" ||
        document.querySelector("input#mail.emailbox-input.opentip").value ===
          "Đang tải." ||
        document.querySelector("input#mail.emailbox-input.opentip").value ===
          "Đang tải.." ||
        document.querySelector("input#mail.emailbox-input.opentip").value ===
          "Đang tải..."
      ) {
        console.log("chưa loat xong mail");
        settime(pasa);
      } else {
        console.log("lấy thành công mail");
        document.querySelector("h2").innerText = "copydone";
        settime(1000);
      }
    }, 1000);
  }
}
settime(1);
// get email fb

function settime(pasa) {
  if (pasa < 1000) {
    setTimeout(() => {
      pasa = pasa + 1;
      if (
        document.querySelector(
          "#tm-body > main > div.container > div > div.col-sm-12.col-md-12.col-lg-12.col-xl-8 > div.tm-content > div > div.inboxWarpMain > div > div.inbox-dataList > ul > li:nth-child(2) > div:nth-child(1) > a > span.inboxSenderEmail.inboxSenderEllipsis"
        )
      ) {
        if (
          document.querySelector(
            "#tm-body > main > div.container > div > div.col-sm-12.col-md-12.col-lg-12.col-xl-8 > div.tm-content > div > div.inboxWarpMain > div > div.inbox-dataList > ul > li:nth-child(2) > div:nth-child(1) > a > span.inboxSenderEmail.inboxSenderEllipsis"
          ).innerText === "registration@facebookmail.com"
        ) {
          document.querySelector("#mail").value = document
            .querySelector(
              "#tm-body > main > div.container > div > div.col-sm-12.col-md-12.col-lg-12.col-xl-8 > div.tm-content > div > div.inboxWarpMain > div > div.inbox-dataList > ul > li:nth-child(2) > div.col-box.hidden-xs-sm > span > a"
            )
            .innerText.slice(0, 5);
          document.querySelector("p").innerText = document
            .querySelector(
              "#tm-body > main > div.container > div > div.col-sm-12.col-md-12.col-lg-12.col-xl-8 > div.tm-content > div > div.inboxWarpMain > div > div.inbox-dataList > ul > li:nth-child(2) > div.col-box.hidden-xs-sm > span > a"
            )
            .innerText.slice(21, 29);
          console.log("lấy thành công mail");
          settime(1000);
        }
      } else {
        console.log("đang đợi mail");
        settime(pasa);
      }
    }, 1000);
  }
}
settime(1);
//sdasd
document.querySelector("p").innerText = document
  .querySelector(
    "#tm-body > main > div.container > div > div.col-sm-12.col-md-12.col-lg-12.col-xl-8 > div.tm-content > div > div.inboxWarpMain > div > div.inbox-dataList > ul > li:nth-child(2) > div:nth-child(1) > a > span.inboxSubject.small.subject-title.d-none.visable-xs-sm"
  )
  .innerText.slice(0, 5);
str = console.log(str.slice(0, 5));

//đổi ngôn ngữ
for (let i = 0; i < 1000; i++) {
  if (document.getElementsByClassName("_5553")[i].innerText === "Tiếng Việt") {
    document.getElementsByClassName("_5553")[i].click();
  }
}
