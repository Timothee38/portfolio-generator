function loadData() {
  for (var i = 0; i < data.length; i++) {
    var category = data[i].category;
    $("#myBtnContainer").append("<button class=\"btn\" onclick=\"filterSelection('" + category + "')\"> " + category + "</button>");
    for (var j = 0; j < data[i].images.length; j++) {
      var img = data[i].images[j];
      $("#myGrid").append("<div class=\"column " + category + "\"><div class=\"content\"><img class=\"clickableImage\" onclick=\"openModal('./img/" + category + "/" + img.fileName + "', '" + img.title + "')\" src=\"./img/" + category + "/" + img.fileName + "\" alt=\"" + img.title + "\" style=\"width:100%\"><h4>" + img.title + "</h4></div></div>");
    }
  }
}

function openModal(filePath, title) {
  $("#myModal").show();
  $("#modalImage").attr("src", filePath)
  $("#imageCaption").html(title);
}

function closeModal() {
  $("#myModal").hide();
}

$(document).click(function(event) {
  if (!$(event.target).closest(".modal-content,.content").length) {
    closeModal()
  }
});

$(document).ready(function() {
  $("#username").html(misc.name);
  loadData();
  filterSelection("all");
});

$(document).attr( 'title', misc.name );
