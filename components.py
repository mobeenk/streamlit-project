




def admin_approval_component(pk):
    html_code = f"""
        <!DOCTYPE html>
        <html>
        <head>
          <title>Remove Button</title>
          <style>
            .remarks-textarea{{
                margin-right:20px;
            }}
            .button-container {{
              display: flex;
              justify-content: center;
              align-items: center;
              height: 100vh;
            }}

            .button-container button {{
              padding: 10px 20px;
              border: none;
              border-radius: 4px;
              cursor: pointer;
            }}

            .reject-button {{
              background-color: #f44336;
              color: white;
              margin-right: 10px;
            }}

            .approve-button {{
              background-color: green;
              color: white;
            }}

            .reject-button:hover {{
              background-color: #d32f2f;
            }}

            .approve-button:hover {{
              background-color: #43a047;
            }}
          </style>
          <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
          <script>
            $(document).ready(function() {{
              // Add click event handler to the reject button
              $('#rejectButton').click(function() {{
                // Show the confirm dialog
                var confirmed = confirm("Are you sure you want to reject?");
                if (confirmed) {{
                  // Get the remarks from the textarea
                  var remarks = $('#remarksTextarea').val();

                  // Make the HTTP DELETE request to the API
                  $.ajax({{
                    url: 'https://jsonplaceholder.com/posts/',
                    type: 'POST',
                    data: {{
                      title: 'Approved',
                      remarks: remarks
                    }},
                    success: function(response) {{
                       alert('Request has been rejected' + JSON.stringify(response));
                    }},
                    error: function(xhr, status, error) {{
                      alert('Failed');
                      console.log(error);
                    }}
                  }});
                }}
              }});

              // Add click event handler to the approve button
              $('#approveButton').click(function() {{
                // Show the confirm dialog
                var confirmed = confirm("Are you sure you want to approve?");
                if (confirmed) {{
                  // Get the remarks from the textarea
                  var remarks = $('#remarksTextarea').val();

                  // Make the HTTP POST request to the API
                  $.ajax({{
                    url: 'https://jsonplaceholder.typicode.com/posts',
                    type: 'POST',
                    data: {{
                      title: 'Returned',
                      remarks: remarks
                    }},
                    success: function(response) {{
                       alert('Request has been approved' + JSON.stringify(response));
                    }},
                    error: function(xhr, status, error) {{
                      alert('Failed');
                      console.log(error);
                    }}
                  }});
                }}
              }});
            }});
          </script>
        </head>
        <body>
          <div class="button-container">
           <textarea id="remarksTextarea" class="remarks-textarea" placeholder="Remarks"></textarea>
            <button class="reject-button" id="rejectButton">Return</button>
            <button class="approve-button" id="approveButton">Approve</button>
          </div>
        </body>
        </html>
        """

    return html_code

