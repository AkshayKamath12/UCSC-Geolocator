import PropTypes from "prop-types";
import React from "react";
import { ButtonGroup } from "./components/ButtonGroup";
import { TextContentTitle } from "./components/TextContentTitle";

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

HeroActions.propTypes = {
  platform: PropTypes.oneOf(["desktop", "mobile"]),
  textContentTitleTitle: PropTypes.string,
  textContentTitleSubtitle: PropTypes.string,
  buttonGroupAlign: PropTypes.string,
  buttonGroupText: PropTypes.string,
};

export const BuildingBlocks = () => {
  return (
    <div className="flex items-center relative rounded-xl overflow-hidden">
      <div className="flex items-center gap-4 p-4 relative flex-1 self-stretch grow">
        <div className="flex flex-col items-start gap-1 relative flex-1 grow">
          <div className="relative self-stretch mt-[-1.00px] font-m3-title-medium font-[number:var(--m3-title-medium-font-weight)] text-[#1d1b20] text-[length:var(--m3-title-medium-font-size)] tracking-[var(--m3-title-medium-letter-spacing)] leading-[var(--m3-title-medium-line-height)] [font-style:var(--m3-title-medium-font-style)]">
            Street View Geolocator
          </div>

          <div className="relative self-stretch font-m3-body-medium font-[number:var(--m3-body-medium-font-weight)] text-[#1d1b20] text-[length:var(--m3-body-medium-font-size)] tracking-[var(--m3-body-medium-letter-spacing)] leading-[var(--m3-body-medium-line-height)] [font-style:var(--m3-body-medium-font-style)]">
            Powered by Google Maps™
          </div>
        </div>
      </div>

      <div className="relative self-stretch w-20 bg-[url(/media.png)] bg-[100%_100%]" />
      <HeroActions platform="desktop" />
    </div>
  );
};