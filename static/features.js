// Remove specific account or entry
$('.remove_form').submit( (evt) => {  
  const removeMessage = confirm('Warning! You are about to remove this permanently!');
  removeMessage;
  if (removeMessage == false) {
    evt.preventDefault();
  }
});

$('.specific_row').hover(
  function() {
    $(this).css('background-color', 'yellow');
  }, function() {
    $(this).css('background-color', 'white');
  }
);


// This below current find all the entry_id and put into a set
const allEntryId = document.querySelectorAll('#entry_id');
const setOfEntryId = new Set ();
for (const item of allEntryId) {
  setOfEntryId.add(item.innerHTML);
};
console.log(setOfEntryId); 
// if the entry that is currently hovered has the same entry.entry_id
// highlight them in the same color