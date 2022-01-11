// Add CSS by JavaScript
var importStyle = function importStyle(b){
    var a = document.createElement("style");
    var c = document;
    c.getElementsByTagName("head")[0].appendChild(a);
    if(a.styleSheet){
        a.styleSheet.cssText = b
    } else {
        a.appendChild(c.createTextNode(b))
    }
};

// Show Menu
function Show_Menu() {
    $(".menu").slideDown("fast");
    $(".menu").css("display", "inline-flex");
    importStyle(".menu-dropdown, .menu {flex-direction: column;} .hide-menu {display: initial} .show-menu {display: none;}")
}
// Hide Menu
function Hide_Menu() {
    $(".menu").slideUp("fast");
    importStyle(".show-menu {display: initial;} .hide-menu {display: none;}")
}

// Middle-Right Marquee
$('.middle-right-marquee').marquee({
	// Duration in milliseconds of the marquee
	//duration: 15000,
    speed: 12,
	// Gap in pixels between the tickers
	gap: 100,
	// Time in milliseconds before the marquee will start animating
	delayBeforeStart: 0,
	// 'left' or 'right' or 'up' or 'down'
	direction: 'up',
	// True or false - should the marquee be duplicated to show an effect of continues flow
	duplicated: true,
    pauseOnHover: true
});

// Bootstrap Toasts
num_of_toasts = 2
for (let show_toasts_start = 1; show_toasts_start <= num_of_toasts; show_toasts_start++) {
    var ToastElement = document.getElementById("toast-" + show_toasts_start);
    //var ToastElement = $("#toast-" + show_toasts_start);
    var MyToast = new bootstrap.Toast(ToastElement);
    MyToast.show();
}

// Bootstrap Tooltips
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
})