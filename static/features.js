// Confirm window for removing specific account or entry
$('.remove_form').submit( (evt) => {  
  const removeMessage = confirm('Warning! You are about to remove this permanently!');
  removeMessage;
  if (removeMessage == false) {
    evt.preventDefault();
  }
});

// Highlight entries with the same entry_id
const entryRows= $('tr.entry_rows');
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