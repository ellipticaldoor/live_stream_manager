$(document).ready(function() {
	time = 1000 * 60 * 60;
	now = new Date();

	var clock = $('#clock');

	clock.countdown(now.getTime() + time);

	clock.on('update.countdown', function(event) {
		var totalHours = event.offset.totalDays * 24 + event.offset.hours;
		$(this).html(event.strftime(totalHours + ' hr  %M min  %S seg'));
	});

	clock.on('finish.countdown', function(event) {
		console.log('finished ;)');
		$('#timer').hide();
		$('#video').show();

		autoPlayVideo('Qi7KDOAj4Xo','100%','100%');
	});
});

function autoPlayVideo(vcode, width, height){
	"use strict";
	$("#video").html('<iframe width="'+width+'" height="'+height+'" src="https://www.youtube.com/embed/'+vcode+'?autoplay=1&loop=1&rel=0&wmode=transparent" frameborder="0" allowfullscreen wmode="Opaque"></iframe>');
}
