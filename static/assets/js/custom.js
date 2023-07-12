function MakeComment(articleId){
    var comment   = $('#CommentText').val()
    $.get('/articles/new_comment' , {
        article_comment   : comment ,
        articleId   : articleId ,
        parent   : null
    }).then(res => console.log(res))
    
}
