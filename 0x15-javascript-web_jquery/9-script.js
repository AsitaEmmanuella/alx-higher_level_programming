$.ajax({
    type: 'POST',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: (translation) => {
      $('DIV#hello').text(translation.hello);
    },
    error: () => {
      console.log('Error loading orders');
    }
  });
  