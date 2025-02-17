/*
We're constantly improving the code you see. 
Please share your feedback here: https://form.asana.com/?k=uvp-HPgd3_hyoXRBw1IcNg&d=1152665201300829
*/

import React from "react";
import { ButtonGroup } from "../ButtonGroup";
import { TextContentTitle } from "../TextContentTitle";

export const HeroActions = ({
  platform,
  textContentTitleTitle = "Title",
  textContentTitleSubtitle = "Subtitle",
  buttonGroupButtonClassName,
  buttonGroupAlign = "justify",
  buttonGroupText = "Button",
  buttonGroupButtonClassNameOverride,
}) => {
  return (
    <div
      className={`w-[var(--responsive-device-width)] flex flex-col items-center gap-[var(--size-space-800)] bg-color-background-default-secondary relative ${platform === "mobile" ? "pt-[var(--size-space-4000)] pr-[var(--size-space-400)] pb-[var(--size-space-4000)] pl-[var(--size-space-400)]" : "pt-[var(--size-space-4000)] pr-[var(--size-space-600)] pb-[var(--size-space-4000)] pl-[var(--size-space-600)]"}`}
      data-responsive-mode={platform === "mobile" ? "mobile" : undefined}
    >
      <TextContentTitle
        align="center"
        className="!flex-[0_0_auto]"
        divClassName={
          platform === "mobile"
            ? "!tracking-[var(--title-page-letter-spacing)] !text-[length:var(--title-page-font-size)] ![font-style:var(--title-page-font-style)] !font-[number:var(--title-page-font-weight)] !font-title-page !leading-[var(--title-page-line-height)]"
            : undefined
        }
        subtitle={textContentTitleSubtitle}
        title={textContentTitleTitle}
      />
      <ButtonGroup
        align={buttonGroupAlign}
        buttonClassName={buttonGroupButtonClassNameOverride}
        buttonClassNameOverride={buttonGroupButtonClassName}
        className="!flex-[0_0_auto]"
        divClassName="!text-color-text-default-default"
        text={buttonGroupText}
      />
    </div>
  );
};
