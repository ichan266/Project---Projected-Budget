//@ Declaring Variables //
// Assign rows of entries into a variable, entryRows
const entryRows = $('tr.entry_rows');

//@ Assign all amounts as a list of jQuery elements into a variable, amounts
const amounts = $('td.amount');   // This is used for inline form with AJAX
const amountValues = $('span.amount_value');   // This is used for displaying amount correctly

//@ Assign all projected balances as a list of jQuery elements into a variable, projectedBalance
const projectedBalances = $('td.projected_balance');


/// *** Homepage - Sign-Up Password Confirmation *** ///
$('#create_user').submit((evt) => {
  if ($('#new_password').val() !== $('#new_password_conf').val()) {
    const unMatchPW = alert('Passwords do not match. Please try again.');
    unMatchPW;
    evt.preventDefault();
  } 
})

/// *** Profile Page & Account Details Page *** ///
// Confirm window for removing specific account or entry
$('.remove_form').submit( (evt) => {  
  const removeMessage = confirm('Warning! You are about to remove this permanently!');
  removeMessage;
  if (removeMessage == false) {
    evt.preventDefault();
  }
});


/// *** Account Details Page *** ///
// Display Balances with $ and comma separator & Highlight in red if negative
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

// Display amounts with income as green and expense as red
const displayAmounts = (jElements) => {
  for (const item of jElements) {
    item.innerText = new Intl.NumberFormat('us-US', {style: 'currency', currency: 'USD', minimumFractionDigits:0}).format(Number(item.innerText));
    if ((+(item.innerText.replace(/[^\-0-9\.]+/g, ""))) <= 0) {
      $(item).css('color', 'rgb(243, 135, 34)');
    } else {
      $(item).css('color', 'rgb(0, 138, 0)');
    };
  };
}

// Enable tooltip
$(function () {
  $('[data-toggle="tooltip"]').tooltip();
});

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
displayAmounts(amountValues);


// Edit Entry Form Part 1: 
// Show the form
for (const item of amounts) {
  $(item).on('click', (evt) => {
    $(this).attr('style', 'None');
    const singleForm = $(evt.target.querySelector('.amount_form'));
    singleForm.show();
    $(evt.target.querySelector('.new_amount')).focus();
  });
};

// Edit Entry Form Part 2: 
// Use AJAX to submit data and recalculate projected balance
for (const item of amounts) {
  $(item).submit( (evt) => {
    evt.preventDefault();
    const formInputs = $(evt.target).serialize();
    $.post('/handle_entry_edit', formInputs, (res) => {
      evtAmountValue = evt.target.parentElement.querySelector('#amount_value')
      evtAmountValue.innerText = res;
      let balance = 0;
      for (const item of document.querySelectorAll('.entry_rows')) {
        let current_amount = +(item.querySelector('.amount_value').innerText.replace(/[^\-0-9\.]+/g, ''));
        balance = current_amount + balance;
        item.querySelector('.projected_balance').innerText = `${balance}`;
      };
      $('.amount_form').hide();
      displayBalances(projectedBalances);
      evtAmountValue.innerText = new Intl.NumberFormat('us-US', {style: 'currency', currency: 'USD', minimumFractionDigits:0}).format(Number(item.innerText));
    });
  });
};
