// 2023.12.02

type JSONValue =
  | null
  | boolean
  | number
  | string
  | JSONValue[]
  | { [key: string]: JSONValue };

function argumentsLength(...args: JSONValue[]): number {
  let len = 0;
  for (let item in args) len++;

  return len;
}
