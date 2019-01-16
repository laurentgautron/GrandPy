$('form').keydown(function(e) {
    if (e.keyCode === 13) {
       $.ajax({
            url: "/answer",
            data: {question: $('#search').val()},
            type: "POST",
            success: function (resp) {
                if (resp !== {}) {
                    $responseDiv = $('#response');
                    $responseDiv.append("<p class='usermessage'>" + $('#search').val() + "</p>");
                    $responseDiv.append("<p class='botmessage'> oui, je connais l'adresse de " + resp['place'] + "</p>");
                    $responseDiv.append("<p id='map' class='map'></p>");
                    displayMap(resp['coord']);
                    $responseDiv.scrollTop($responseDiv[0].scrollHeight);
                }
                else {
                    $responseDiv.append("<p class='botmessage'> non, je ne connais pas l'adresse de" + $('#search').val() + "</p>")
                }
                $('form')[0].reset();
            }
        });
        e.preventDefault();
    }
});