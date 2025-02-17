/*
We're constantly improving the code you see. 
Please share your feedback here: https://form.asana.com/?k=uvp-HPgd3_hyoXRBw1IcNg&d=1152665201300829
*/

import React from "react";

export const ButtonGroup = ({
  buttonEnd = true,
  buttonStart = true,
  align,
  className,
  buttonClassName,
  divClassName,
  text = "Button",
  buttonClassNameOverride,
}) => {
  return (
    <button
      className={`all-[unset] box-border w-60 flex items-center gap-[var(--size-space-400)] relative ${align === "center" ? "justify-center" : ""} ${className}`}
    >
      {buttonStart && (
        <button
          className={`all-[unset] box-border items-center gap-[var(--size-space-200)] pt-[var(--size-space-300)] pr-[var(--size-space-300)] pb-[var(--size-space-300)] pl-[var(--size-space-300)] overflow-hidden rounded-[var(--size-radius-200)] justify-center relative ${align === "justify" ? "flex" : "inline-flex"} ${align === "justify" ? "grow" : ""} ${align === "justify" ? "flex-1" : "flex-[0_0_auto]"} ${buttonClassName}`}
        >
          <div
            className={`font-single-line-body-base w-fit mt-[-1.00px] tracking-[var(--single-line-body-base-letter-spacing)] text-[length:var(--single-line-body-base-font-size)] [font-style:var(--single-line-body-base-font-style)] text-color-text-neutral-default font-[number:var(--single-line-body-base-font-weight)] leading-[var(--single-line-body-base-line-height)] whitespace-nowrap relative ${divClassName}`}
          >
            {text}
          </div>
        </button>
      )}

      {buttonEnd && (
        <button
          className={`all-[unset] box-border border border-solid border-color-border-brand-default items-center gap-[var(--size-space-200)] pt-[var(--size-space-300)] pr-[var(--size-space-300)] pb-[var(--size-space-300)] pl-[var(--size-space-300)] overflow-hidden rounded-[var(--size-radius-200)] justify-center bg-[color:var(--color-background-brand-default)] relative ${align === "justify" ? "flex" : "inline-flex"} ${align === "justify" ? "grow" : ""} ${align === "justify" ? "flex-1" : "flex-[0_0_auto]"} ${buttonClassNameOverride}`}
        >
          <div className="font-single-line-body-base w-fit mt-[-1.00px] tracking-[var(--single-line-body-base-letter-spacing)] text-[length:var(--single-line-body-base-font-size)] [font-style:var(--single-line-body-base-font-style)] text-color-text-brand-on-brand font-[number:var(--single-line-body-base-font-weight)] leading-[var(--single-line-body-base-line-height)] whitespace-nowrap relative">
            {text}
          </div>
        </button>
      )}
    </button>
  );
};
