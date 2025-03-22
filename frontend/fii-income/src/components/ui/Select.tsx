import { ReactNode } from "react";

interface SelectProps extends React.SelectHTMLAttributes<HTMLSelectElement> {
  children: ReactNode;
}


export function Select({ children, ...props }: SelectProps) {
    return <select className="border p-2 rounded w-full" {...props}>{children}</select>;
}