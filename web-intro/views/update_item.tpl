<html>
    <body>
        <hr/>
        <form action="/update" method="POST">
            <label for="id_input">ID:</label>
            <input id="id_input" name="id" value="{{ item['id'] }}"/>

            <label for="description_input">Description:</label>
            <input id="description_input" name="description" value="{{ item['description'] }}"/>
            <div>
                <button type="submit">Submit</button>
            </div>
        </form>
        <hr/>
    </body>
</html>