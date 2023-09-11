<html>
    <body>
        <h1>Shopping List</h1>
        <hr>
        <table>
            <tbody>
                % for item in shopping_list:
                    <tr>
                        <td>{{ str(item['description']) }}</td>
                        <td><a href="/update/{{item['id']}}">Update</a></td>
                        <td><a href="/delete/{{item['id']}}">Delete</a></td>
                    </tr>
                % end
            </tbody>
        </table>
        <hr>
        <a href="/add">Add item</a>
    </body
</html>