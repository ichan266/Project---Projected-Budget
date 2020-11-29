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

// AJAX:Handle Entry Amount Edit
for (const item of $('.amount')) {   
  $(item).on('click', (evt) => {
    $(this).attr('style', "None");
    const singleForm = $(evt.target.querySelector('.amount_form'));
    console.log(`singleForm = `, singleForm)
    singleForm.show();
    
  });
};

for (const item of $('.amount_form')) {
  $(item).submit( (evt) => {
    evt.preventDefault();
    const formInputs = $(evt.target).serialize();
    $.post('/handle_entry_edit', formInputs, (res) => {
      evt.target.parentElement.querySelector('.amount_value').innerText = res;
      let balance = 0;
      for (const item of document.querySelectorAll('.entry_rows')) {
        let current_amount = Number(item.querySelector('.amount_value').innerText);
        balance = current_amount + balance;
        item.querySelector('.projected_balance').innerText = balance;
      };
      $('.amount_form').hide();
    });
  });
};
