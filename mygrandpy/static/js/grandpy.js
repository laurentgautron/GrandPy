$('form').keydown(function(e) {
    if (e.keyCode === 13) {
       $.ajax({
            url: "/answer",
            data: {question: $('#search').val()},
            type: "POST",
            success: function (resp) {
                $responseDiv = $('#response');
                $responseDiv.append("<p> oui, je connais l'adresse de " + resp['place'] + "</p>");
                $responseDiv.scrollTop($responseDiv[0].scrollHeight);
                console.log(resp);
                displayMap(resp['coord']);
                $('form')[0].reset();
            }
        });
        e.preventDefault();
    }
});