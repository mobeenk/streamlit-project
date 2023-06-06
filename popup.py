

def popup_message():
    popup_html = '''
        <!DOCTYPE html>
<html>
<head>

  <style>
    .dialog-button {
      padding: 10px 20px;
      font-size: 16px;
    }
  </style>
</head>
<body>

  
  <button class="dialog-button" onclick="openDialog()">Open Dialog</button>

  <dialog id="myDialog">
    <h2>Dialog Title</h2>
    <p>This is the content of the dialog.</p>
    <button onclick="closeDialog()">Close</button>
  </dialog>

  <script>
    function openDialog() {
      var dialog = document.getElementById("myDialog");
      dialog.showModal();
    }

    function closeDialog() {
      var dialog = document.getElementById("myDialog");
      dialog.close();
    }
  </script>
</body>
</html>


    '''
    return popup_html