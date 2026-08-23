import * as React from "react";
export const Drawer = ({ children, open, onOpenChange }: any) => <div data-open={open}>{children}</div>;
export const DrawerContent = ({ children, className }: any) => <div className={className}>{children}</div>;
export const DrawerHeader = ({ children, className }: any) => <div className={className}>{children}</div>;
export const DrawerTitle = ({ children, className }: any) => <div className={className}>{children}</div>;
export const DrawerDescription = ({ children, className }: any) => <div className={className}>{children}</div>;
export const DrawerFooter = ({ children, className }: any) => <div className={className}>{children}</div>;
export const DrawerClose = ({ children, asChild }: any) => <div>{children}</div>;
