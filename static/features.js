// Confirm window for removing specific account or entry
$('.remove_form').submit( (evt) => {  
  const removeMessage = confirm('Warning! You are about to remove this permanently!');
  removeMessage;
  if (removeMessage == false) {
    evt.preventDefault();
  }
});


/// *** Account Details Page *** ///
// Assign rows of entries into a variable, entryRows
const entryRows= $('tr.entry_rows');

// Highlight entries with the same entry_id
for (const item of entryRows) {
  let sameEntryId = [];
  $(item).hover(
    function() {
      for (entry of entryRows) {
        if (item.cells.entry_id.innerText === entry.cells.entry_id.innerText) {
          sameEntryId.push(entry);
        };
      }
      $(sameEntryId).css('background-color', '#3399ff');
    }, function() {
      $(sameEntryId).css('background-color', 'white');
    }
  );
}

// // AJAX:Handle Entry Amount Edit
// $('edit_form').on('click', () => {
//   for (const item of entryRows) {
//     $('#amount').replaceWith('<form><input id="amount" type="number" name="new_amount" placeholder="New Amount"><input type="submit"></form>');
//     $.get('/handle_entry_edit', (response) => {
//       for (entry of entryRows) {
//         $('#amount').text(response);
//       };
//     }); 
//   };
// });


