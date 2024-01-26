export default function guardrail(mathFunction) {
  const queue = [];
  try {
    const func = mathFunction();
    queue.push(func);
  } catch (error) {
    queue.push(`Error: ${error.message}`);
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}
