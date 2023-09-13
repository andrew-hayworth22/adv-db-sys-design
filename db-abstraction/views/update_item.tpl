<html>
    <body>
        <hr/>
        <form action="/update" method="POST">
            <input id="id_input" type="hidden" name="id" value="{{ item['id'] }}"/>

            <label for="description_input">Description:</label>
            <input id="description_input" name="description" value="{{ item['description'] }}"/>
            <div>
                <button type="submit">Submit</button>
            </div>
        </form>
        <hr/>
    </body>
</html>