const removeForm = $('.remove_form');

removeForm.submit( (evt) => {  
  const removeMessage = confirm('Warning! You are about to remove this permanently!');
  removeMessage;
  if (removeMessage == false) {
    evt.preventDefault();
  }

    console.log(evt.target);
});