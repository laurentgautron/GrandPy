$('form').keydown(function(e) {
    if (e.keyCode == 13) {
        $.ajax({
            url: "/answer",
            data: {question: $('#search').val()},
            type: "POST",
            success: function (resp) {
                $responseDiv = $('#response');
                $responseDiv.append("<p>Bonjour: " + resp + "</p>");
                $responseDiv.scrollTop($responseDiv[0].scrollHeight);
                $('form')[0].reset();
            }
        });
        e.preventDefault();
    }
});