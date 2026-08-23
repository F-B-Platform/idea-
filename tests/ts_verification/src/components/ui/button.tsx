import * as React from "react";
export const Button = React.forwardRef<HTMLButtonElement, any>(({ className, variant, size, children, ...props }, ref) => (
  <button ref={ref} className={className} {...props}>{children}</button>
));
