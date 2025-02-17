/*
We're constantly improving the code you see. 
Please share your feedback here: https://form.asana.com/?k=uvp-HPgd3_hyoXRBw1IcNg&d=1152665201300829
*/

import React from "react";

export const TextContentTitle = ({
  title = "Title",
  hasSubtitle = true,
  subtitle = "Subtitle",
  align,
  className,
  divClassName,
}) => {
  return (
    <div
      className={`inline-flex flex-col items-center gap-[var(--size-space-200)] relative ${className}`}
    >
      <div
        className={`relative self-stretch mt-[-1.00px] font-title-hero font-[number:var(--title-hero-font-weight)] text-color-text-default-default text-[length:var(--title-hero-font-size)] text-center tracking-[var(--title-hero-letter-spacing)] leading-[var(--title-hero-line-height)] [font-style:var(--title-hero-font-style)] ${divClassName}`}
      >
        {title}
      </div>

      {hasSubtitle && (
        <div className="relative self-stretch font-subtitle font-[number:var(--subtitle-font-weight)] text-color-text-default-secondary text-[length:var(--subtitle-font-size)] text-center tracking-[var(--subtitle-letter-spacing)] leading-[var(--subtitle-line-height)] [font-style:var(--subtitle-font-style)]">
          {subtitle}
        </div>
      )}
    </div>
  );
};
