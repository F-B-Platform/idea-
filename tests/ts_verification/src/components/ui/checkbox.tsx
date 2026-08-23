import * as React from "react";

export const Checkbox = ({ id, checked, onCheckedChange, className }: { id: string; checked: boolean; onCheckedChange: (checked: boolean) => void; className?: string }) => (
  <input type="checkbox" id={id} checked={checked} onChange={(e) => onCheckedChange(e.target.checked)} className={className} />
);
