import { render, screen } from '@testing-library/react';
import TableBody from './TableBody';
import TableHeaders from './TableHeaders';
import mockJson from "./testData/mockData.json"

test('renders table headers', () => {
  render(<table><thead><TableHeaders/></thead><tbody></tbody></table>);

  const linkElement = screen.getByRole('row');
  expect(linkElement.outerHTML).toEqual("<td><th scope=\"col\">Trace ID</th><th scope=\"col\">Name</th><th scope=\"col\">Order</th><th scope=\"col\">Started Status</th><th scope=\"col\">Processing Status</th></tr>");
});

test('renders table rows with success and failure', () => {
  render(<table><TableBody jsonData={mockJson}/></table>);

  const linkElement = screen.getByRole('row');
  expect(linkElement.outerHTML).toEqual("<tr><td>23404</td><td>SherlockHolmes</td><td>Pie</td><td><span class=\"success\">✓</span></td><td><span class=\"failure\">✗</span></td></tr>");
});
