window.onload = function () {
    const $myList = $('UL.my_list');

    $('DIV#add_item').click(() => {
      $myList.append('<li>Item</li>');
    });
  
    $('DIV#remove_item').click(() => {
      const lastItem = $('UL.my_list LI').last();
      lastItem.remove();
    });
  
    $('DIV#clear_list').click(() => {
      $myList.empty();
    });
  };
  