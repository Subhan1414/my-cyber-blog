// Google Analytics standard gtag.js GA4 loader (replace 'G-XXXXXXXXXX' with your real Measurement ID)
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-G8FJQPDE4D'); // <- Replace with your GA4 code

// Track CV (e.g. cv.docx) downloads as GA4 events
document.addEventListener('DOMContentLoaded', function() {
  // Select all links ending with cv.docx (update filename if needed)
  var cvLinks = document.querySelectorAll('a[href$="cv.docx"]');
  cvLinks.forEach(function(link) {
    link.addEventListener('click', function() {
      if (typeof gtag === 'function') {
        gtag('event', 'download', {
          'event_category': 'CV',
          'event_label': 'cv.docx'
        });
      }
    });
  });
});

