// Enable tooltip
$(function () {
  $('[data-toggle="tooltip"]').tooltip();
});

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
const entryRows = $('tr.entry_rows');

// Assign all amounts as a list of jQuery elements into a variable, amounts
const amounts = $('td.amount')

// Assign all projected balances as a list of jQuery elements into a variable, projectedBalance
const projectedBalances = $('td.projected_balance');


// Display Amounts and Projected Balances with $ and comma separator
const displayBalances = (jElements) => {
  for (const item of jElements) {
    item.innerText = new Intl.NumberFormat('us-US', {style: 'currency', currency: 'USD', minimumFractionDigits:0}).format(Number(item.innerText));
    if ((+(item.innerText.replace(/[^\-0-9\.]+/g, ""))) <= 0) {
      $(item).css('color', 'red');
    } else {
      $(item).css('color', 'black');
    };
  };
}


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
      $(sameEntryId).css('background-color', '#c9ccf7');
    }, function() {
      $(sameEntryId).css('background-color', '');
    }
  );
}

// Highlight projected balances that are below zero in red
displayBalances(projectedBalances);


// Edit Entry Form Part 1: 
// Show the form
for (const item of $('.amount')) {   
  $(item).on('click', (evt) => {
    $(this).attr('style', "None");
    const singleForm = $(evt.target.querySelector('.amount_form'));
    singleForm.show();
    $(evt.target.querySelector('.new_amount')).focus();
  });
};

// Edit Entry Form Part 2: 
// Use AJAX to submit data and recalculate projected balance
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
        item.querySelector('.projected_balance').innerText = `${balance}`;
      };
      $('.amount_form').hide();
    });
  });
};