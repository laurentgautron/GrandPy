$('form').submit( function (e) {
    console.log("c'est moi");
    let question = $('#response p:last').text().split(" ");
    console.log('la question affichée: ' + question);
    console.log('le mot: ' + $('#search').val());
    let pos = question.push($('#search').val());
    console.log('la position du mot: ' + pos);
    let sup = question.splice(pos,1);
    console.log(sup);
    console.log(question);
    $.post("/wordcollection", {word:question}, function(rep) {
        $('form')[0].reset();
        $('#response').append('<p>' + rep + '</p>');
    });
    e.preventDefault();
});