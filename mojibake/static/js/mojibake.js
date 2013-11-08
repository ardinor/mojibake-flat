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
    if (window.location.pathname.indexOf("archive") !== -1)
    {
        $('li.active').removeClass();
        $('#archive_tab').addClass('active');
    }
    if (window.location.pathname.indexOf("tags") !== -1)
    {
        $('li.active').removeClass();
        $('#tags_tab').addClass('active');
    }
    if (window.location.pathname.indexOf("categories") !== -1)
    {
        $('li.active').removeClass();
        $('#categories_tab').addClass('active');
    }
});
