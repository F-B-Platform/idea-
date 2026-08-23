import * as React from "react";

export const RadioGroup = ({ value, onValueChange, className, children }: { value: string; onValueChange: (val: string) => void; className?: string; children: React.ReactNode }) => (
  <div className={className}>{children}</div>
);

export const RadioGroupItem = ({ value, id, className }: { value: string; id: string; className?: string }) => (
  <input type="radio" value={value} id={id} className={className} />
);
