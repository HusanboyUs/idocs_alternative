import sqlite3
from jinja2 import Template
from datetime import datetime

class TimeGenerate:


    @staticmethod
    def main():
        conn = sqlite3.connect('timedb.sqlite3')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM times')
        data = cursor.fetchall()
        conn.close()

        # Define the HTML template
        html_template = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Total Times</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
        </head>
        <body data-bs-theme="dark">

            <div class="col-md-6 offset-md-3 mt-5">
                <h1>Total Times</h1>
                <br>
            
                <table class="table table-striped">
                    <tr>
                        <th>User</th>
                        <th>Logged Time</th>
                        <th>Logged Date</th>
                    </tr>
                    {% for row in data %}
                        <tr>
                            <td>{{ row[0] }}</td>
                            <td class="number">{{ row[1] }}</td>
                            <td>{{ row[2] }}</td>
                        </tr>
                    {% endfor %}
                <tbody>
                <br>
                <div class="alert alert-success" role="alert" id='result'>
                    
                </div>
            </div>
             <script>
                var numberElements = document.getElementsByClassName("number");

                // Initialize sum
                var sum = 0;

                // Loop through each element
                for (var i = 0; i < numberElements.length; i++) {
                    // Get the text content of the element
                    var numberString = numberElements[i].textContent;

                    // Extract and sum individual digits
                    for (var j = 0; j < numberString.length; j++) {
                        var char = numberString.charAt(j);
                        if (!isNaN(char)) {
                            sum += parseInt(char, 10);
                        }
                    }
                }
                document.getElementById('result').textContent = 'Total: ' + sum;
            </script>
        </body>
        </html>
        """

        template = Template(html_template)
        rendered_html = template.render(data=data)
        with open('output.html', 'w') as f:
            f.write(rendered_html)

