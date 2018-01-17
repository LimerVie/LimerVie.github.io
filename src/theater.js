var theater = new theaterJS();
  var theater = theaterJS()
  
  theater
    .on('type:start, erase:start', function () {
      var actor = theater.getCurrentActor()
      actor.$element.classList.add('is-typing')
    })
    .on('type:end, erase:end', function () {
      var actor = theater.getCurrentActor()
      actor.$element.classList.remove('is-typing')
    })
  
  theater
    .addActor('vader')
    
  theater
    .addScene('vader:<h4>hi, I\'m <strong>Wincer</strong><small> /ˈwɪnsə(r)/</small></h4>', { accuracy: 0.4, speed: 0.1 })