/**
 * Created by mmontalto1 on 31/01/2015.
 */
$(document).ready(function() {
    var end = Date.parse("23 Feb 2015 5:00:00 +0100");
    var now = Date.now();
    var remainingSeconds = (end - now) / 1000;
    var clock = $('.your-clock').FlipClock(remainingSeconds, {
        // ... your options here
        countdown: true,
        clockFace: 'DailyCounter'
    });
});