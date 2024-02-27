export default function TableBody({jsonData}) {
  return (
    <tbody>
        {jsonData.map((order, key) => (
            <tr key={key}>
                <td>{order.trace_id}</td>
                <td>{order.abbreviated_name}</td>
                <td>{order.food_ordered}</td>
                <td><Status status={order.started_status}/></td>
                <td><Status status={order.processing_status}/></td>
            </tr>
        ))}
    </tbody>
  );
}

function Status({status}) {
    if (status === 'True') {
        return <span className="success">&#10003;</span>;
      
    } else {
        return <span className="failure">&#10007;</span>;
    }
}