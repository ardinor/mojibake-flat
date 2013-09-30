$(function() {
    if (window.location.pathname === "/")
    {
        $('li.active').removeClass();
        $('#home_tab').addClass('active');
    }
    if (window.location.pathname.indexOf("posts") !== -1)
    {
        $('li.active').removeClass();
        $('#posts_tab').addClass('active');
    }
    if (window.location.pathname.indexOf("about") !== -1)
    {
        $('li.active').removeClass();
        $('#about_tab').addClass('active');
    }
});
