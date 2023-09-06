<h1> List of Pets </h1>
<ul>
    % for pet in pets:
        <li>{{ pet['name'] }}</li>
    % end
</ul>

<h1> Table of Pets </h1>

<table>
    <thead>
        <th>Name</th>
        <th>Kind</th>
    </thead>

    <tbody>
    % for pet in pets:
        <tr>
            <td>{{pet['name']}}</td>
            <td>{{pet['kind']}}</td>
        </tr>
    % end
    </tbody>
</table>