




def remove_component(pk):
    html_code = f"""
        <!DOCTYPE html>
        <html>
        <head>
          <title>Remove Button</title>
          <style>
            button {{
              padding: 10px 20px;
              background-color: #f44336;
              color: white;
              border: none;
              border-radius: 4px;
              cursor: pointer;
            }}
          </style>
          <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
          <script>
            $(document).ready(function() {{
              // Add click event handler to the remove button
              $('#removeButton').click(function() {{
                // Show the confirm dialog
                var confirmed = confirm("Are you sure you want to delete?");
                if (confirmed) {{
                  // Make the HTTP DELETE request to the API
                  $.ajax({{
                    url: 'https://jsonplaceholder.typicode.com/posts/1',
                    type: 'GET',
                    success: function(response) {{
                       alert('Request has been deleted'+JSON.stringify(response))
                    }},
                    error: function(xhr, status, error) {{
                      alert('Failed')
                      console.log(error)
                    }}
                  }});
                }}
              }});
            }});
          </script>
        </head>
        <body>
          <button style="margin: 25px 0px 0px 120px;" id="removeButton">Remove Plan</button>
        </body>
        </html>
        """

    return html_code

