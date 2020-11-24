$('.remove_form').submit( (evt) => {  
  const removeMessage = confirm('Warning! You are about to remove this permanently!');
  removeMessage;
  if (removeMessage == false) {
    evt.preventDefault();
  }

    console.log(evt.target);
});

$('.specific_row').hover(
  function() {
    $(this).css('background-color', 'yellow');
  }, function() {
    $(this).css('background-color', 'white');
  }
);


const allRecurrentEntries = $("#entry_id").text();
console.log(allRecurrentEntries);
// loop to find all entry_ids
// if the entries has the same entry.entry_id
// highlight them in the same color